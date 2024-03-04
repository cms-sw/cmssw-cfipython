import FWCore.ParameterSet.Config as cms

def WtoLNuSelector(**kwargs):
  mod = cms.EDFilter('WtoLNuSelector',
    electronInputTag = cms.untracked.InputTag('gedGsfElectrons'),
    offlineBeamSpot = cms.untracked.InputTag('offlineBeamSpot'),
    muonInputTag = cms.untracked.InputTag('muons'),
    pfmetTag = cms.untracked.InputTag('pfMetT1T2Txy'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
