import FWCore.ParameterSet.Config as cms

def FedErrorDumper(*args, **kwargs):
  mod = cms.EDAnalyzer('FedErrorDumper',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
