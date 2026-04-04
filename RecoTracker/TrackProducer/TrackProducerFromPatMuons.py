import FWCore.ParameterSet.Config as cms

def TrackProducerFromPatMuons(*args, **kwargs):
  mod = cms.EDProducer('TrackProducerFromPatMuons',
    src = cms.InputTag('slimmedMuons'),
    innerTrackOnly = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
