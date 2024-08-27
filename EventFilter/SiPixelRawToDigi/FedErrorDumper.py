import FWCore.ParameterSet.Config as cms

def FedErrorDumper(**kwargs):
  mod = cms.EDAnalyzer('FedErrorDumper',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
