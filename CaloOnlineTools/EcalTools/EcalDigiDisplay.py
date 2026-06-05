import FWCore.ParameterSet.Config as cms

def EcalDigiDisplay(*args, **kwargs):
  mod = cms.EDAnalyzer('EcalDigiDisplay',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
