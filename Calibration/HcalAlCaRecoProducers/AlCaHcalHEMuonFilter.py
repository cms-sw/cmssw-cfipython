import FWCore.ParameterSet.Config as cms

def AlCaHcalHEMuonFilter(*args, **kwargs):
  mod = cms.EDFilter('AlCaHcalHEMuonFilter',
    prescale = cms.int32(1),
    muonPtCut = cms.double(20),
    muonEtaCut = cms.double(1.305),
    hbheMuonLabel = cms.InputTag('alcaHcalHBHEMuonProducer', 'hbheMuon'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
