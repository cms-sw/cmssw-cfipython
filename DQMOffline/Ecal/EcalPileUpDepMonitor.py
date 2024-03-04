import FWCore.ParameterSet.Config as cms

def EcalPileUpDepMonitor(**kwargs):
  mod = cms.EDProducer('EcalPileUpDepMonitor',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
