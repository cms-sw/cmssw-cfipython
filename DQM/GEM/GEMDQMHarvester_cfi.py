import FWCore.ParameterSet.Config as cms

GEMDQMHarvester = cms.EDProducer('GEMDQMHarvester',
  fromFile = cms.string(''),
  mightGet = cms.optional.untracked.vstring
)
