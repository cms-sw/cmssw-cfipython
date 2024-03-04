import FWCore.ParameterSet.Config as cms

def AlCaHcalHEMuonFilter(**kwargs):
  mod = cms.EDFilter('AlCaHcalHEMuonFilter',
    prescale = cms.int32(1),
    muonPtCut = cms.double(20),
    muonEtaCut = cms.double(1.305),
    hbheMuonLabel = cms.InputTag('alcaHcalHBHEMuonProducer', 'hbheMuon'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
