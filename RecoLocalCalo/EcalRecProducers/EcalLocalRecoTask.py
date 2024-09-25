import FWCore.ParameterSet.Config as cms

def EcalLocalRecoTask(*args, **kwargs):
  mod = cms.EDAnalyzer('EcalLocalRecoTask',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
