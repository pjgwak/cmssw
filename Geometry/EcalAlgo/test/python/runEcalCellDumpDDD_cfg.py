import FWCore.ParameterSet.Config as cms

process = cms.Process("EcalGeometryTest")

process.load("Geometry.HcalCommonData.hcalDDDSimConstants_cff")
process.load("Geometry.HcalCommonData.hcalDDDRecConstants_cfi")
process.load("Geometry.EcalCommonData.ecalSimulationParameters_cff")
process.load("Geometry.CMSCommonData.cmsIdealGeometryXML_cfi");
process.load("Geometry.CaloEventSetup.CaloTopology_cfi")
process.load("Geometry.CaloEventSetup.CaloGeometry_cff")
process.load("Geometry.CaloEventSetup.EcalTrigTowerConstituents_cfi")
process.load("Geometry.EcalMapping.EcalMapping_cfi")
process.load("Geometry.EcalMapping.EcalMappingRecord_cfi")

process.source = cms.Source("EmptySource")
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
    )

process.Timing = cms.Service("Timing")

process.demo1 = cms.EDAnalyzer("ecalBarrelCellParameterDump")
process.demo2 = cms.EDAnalyzer("ecalEndcapCellParameterDump")


process.p1 = cms.Path(process.demo1 * process.demo2)
