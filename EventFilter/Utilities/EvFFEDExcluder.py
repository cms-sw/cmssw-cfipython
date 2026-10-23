import FWCore.ParameterSet.Config as cms

def EvFFEDExcluder(*args, **kwargs):
  mod = cms.EDProducer('EvFFEDExcluder',
    src = cms.InputTag('source'),
    fedsToExclude = cms.vuint32(),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
