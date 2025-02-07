import FWCore.ParameterSet.Config as cms

def HcalHBHENewMuonAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalHBHENewMuonAnalyzer',
    hbheMuonLabel = cms.InputTag('alcaHcalHBHEMuonProducer', 'hbheMuon'),
    useRaw = cms.int32(0),
    maxDepth = cms.untracked.int32(7),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
