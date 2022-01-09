import FWCore.ParameterSet.Config as cms

gemEfficiencyHarvesterDefault = cms.EDProducer('GEMEfficiencyHarvester',
  folder = cms.untracked.string('GEM/Efficiency/type0'),
  mightGet = cms.optional.untracked.vstring
)
