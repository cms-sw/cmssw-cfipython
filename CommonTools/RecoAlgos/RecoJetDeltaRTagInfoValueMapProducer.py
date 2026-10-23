import FWCore.ParameterSet.Config as cms

def RecoJetDeltaRTagInfoValueMapProducer(*args, **kwargs):
  mod = cms.EDProducer('RecoJetDeltaRTagInfoValueMapProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
