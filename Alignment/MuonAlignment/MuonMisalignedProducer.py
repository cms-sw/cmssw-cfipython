import FWCore.ParameterSet.Config as cms

def MuonMisalignedProducer(**kwargs):
  mod = cms.EDAnalyzer('MuonMisalignedProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
