import FWCore.ParameterSet.Config as cms

def TrackProducerFromPatMuons(**kwargs):
  mod = cms.EDProducer('TrackProducerFromPatMuons',
    src = cms.InputTag('slimmedMuons'),
    innerTrackOnly = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
