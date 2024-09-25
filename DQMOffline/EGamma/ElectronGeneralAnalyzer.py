import FWCore.ParameterSet.Config as cms

def ElectronGeneralAnalyzer(*args, **kwargs):
  mod = cms.EDProducer('ElectronGeneralAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
