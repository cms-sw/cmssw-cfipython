import FWCore.ParameterSet.Config as cms

def CATopJetTagger(*args, **kwargs):
  mod = cms.EDProducer('CATopJetTagger',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
