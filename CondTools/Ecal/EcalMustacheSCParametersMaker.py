import FWCore.ParameterSet.Config as cms

def EcalMustacheSCParametersMaker(*args, **kwargs):
  mod = cms.EDAnalyzer('EcalMustacheSCParametersMaker',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
