import FWCore.ParameterSet.Config as cms

nanoAODDQM = cms.EDProducer('NanoAODDQM',
  vplots = cms.PSet(),
  mightGet = cms.optional.untracked.vstring
)
