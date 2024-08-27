import FWCore.ParameterSet.Config as cms

def EvFFEDExcluder(**kwargs):
  mod = cms.EDProducer('EvFFEDExcluder',
    src = cms.InputTag('source'),
    fedsToExclude = cms.vuint32(),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
