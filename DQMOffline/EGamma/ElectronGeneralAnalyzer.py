import FWCore.ParameterSet.Config as cms

def ElectronGeneralAnalyzer(**kwargs):
  mod = cms.EDProducer('ElectronGeneralAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
