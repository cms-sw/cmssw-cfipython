import FWCore.ParameterSet.Config as cms

def AlCaHcalHBHEMuonFilter(*args, **kwargs):
  mod = cms.EDFilter('AlCaHcalHBHEMuonFilter',
    prescale = cms.int32(1),
    minimumMuonP = cms.double(5),
    hbheMuonLabel = cms.InputTag('alcaHcalHBHEMuonProducer', 'hbheMuon'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
