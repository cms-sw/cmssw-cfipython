import FWCore.ParameterSet.Config as cms

def EcalPileUpDepMonitor(*args, **kwargs):
  mod = cms.EDProducer('EcalPileUpDepMonitor',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
