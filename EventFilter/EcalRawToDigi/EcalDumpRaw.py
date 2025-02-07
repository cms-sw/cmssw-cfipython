import FWCore.ParameterSet.Config as cms

def EcalDumpRaw(*args, **kwargs):
  mod = cms.EDAnalyzer('EcalDumpRaw',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
