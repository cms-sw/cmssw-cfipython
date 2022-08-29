import FWCore.ParameterSet.Config as cms

gemEfficiencyHarvester = cms.EDProducer('GEMEfficiencyHarvester',
  confidenceLevel = cms.untracked.double(0.683),
  logCategory = cms.untracked.string('GEMEfficiencyHarvester'),
  folders = cms.untracked.vstring('GEM/Efficiency/muonSTA'),
  mightGet = cms.optional.untracked.vstring
)
