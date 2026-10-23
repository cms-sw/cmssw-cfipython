import FWCore.ParameterSet.Config as cms

def WtoLNuSelector(*args, **kwargs):
  mod = cms.EDFilter('WtoLNuSelector',
    electronInputTag = cms.untracked.InputTag('gedGsfElectrons'),
    offlineBeamSpot = cms.untracked.InputTag('offlineBeamSpot'),
    muonInputTag = cms.untracked.InputTag('muons'),
    pfmetTag = cms.untracked.InputTag('pfMetT1T2Txy'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
