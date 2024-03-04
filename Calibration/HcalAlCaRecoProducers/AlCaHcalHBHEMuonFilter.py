import FWCore.ParameterSet.Config as cms

def AlCaHcalHBHEMuonFilter(**kwargs):
  mod = cms.EDFilter('AlCaHcalHBHEMuonFilter',
    prescale = cms.int32(1),
    minimumMuonP = cms.double(5),
    hbheMuonLabel = cms.InputTag('alcaHcalHBHEMuonProducer', 'hbheMuon'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
