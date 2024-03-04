import FWCore.ParameterSet.Config as cms

def TtSemiLepJetCombMVAFileSource(**kwargs):
  mod = cms.ESSource('TtSemiLepJetCombMVAFileSource',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
