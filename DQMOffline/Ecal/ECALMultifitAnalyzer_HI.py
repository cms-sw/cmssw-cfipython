import FWCore.ParameterSet.Config as cms

def ECALMultifitAnalyzer_HI(*args, **kwargs):
  mod = cms.EDProducer('ECALMultifitAnalyzer_HI',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
