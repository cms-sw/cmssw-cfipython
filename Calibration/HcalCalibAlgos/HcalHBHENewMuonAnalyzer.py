import FWCore.ParameterSet.Config as cms

def HcalHBHENewMuonAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('HcalHBHENewMuonAnalyzer',
    hbheMuonLabel = cms.InputTag('alcaHcalHBHEMuonProducer', 'hbheMuon'),
    useRaw = cms.int32(0),
    maxDepth = cms.untracked.int32(7),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
