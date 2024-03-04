import FWCore.ParameterSet.Config as cms

def MuonKinVsEtaAnalyzer(**kwargs):
  mod = cms.EDProducer('MuonKinVsEtaAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
