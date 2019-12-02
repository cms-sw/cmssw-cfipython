import FWCore.ParameterSet.Config as cms

GEMDQMHarvester = cms.EDProducer('GEMDQMHarvester',
  mightGet = cms.optional.untracked.vstring
)
