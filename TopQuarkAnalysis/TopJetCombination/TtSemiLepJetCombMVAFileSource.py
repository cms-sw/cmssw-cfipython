import FWCore.ParameterSet.Config as cms

def TtSemiLepJetCombMVAFileSource(*args, **kwargs):
  mod = cms.ESSource('TtSemiLepJetCombMVAFileSource',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
