import FWCore.ParameterSet.Config as cms

GEMDQMSource = cms.EDProducer('GEMDQMSource',
  recHitsInputLabel = cms.InputTag('gemRecHits'),
  mightGet = cms.optional.untracked.vstring
)
