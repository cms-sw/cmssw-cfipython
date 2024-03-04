import FWCore.ParameterSet.Config as cms

def SinglePhotonJetPlusHOFilter(**kwargs):
  mod = cms.EDFilter('SinglePhotonJetPlusHOFilter',
    Ptcut = cms.double(90),
    Etacut = cms.double(1.5),
    HOcut = cms.double(5),
    Pho_Ptcut = cms.double(120),
    PFJets = cms.required.InputTag,
    particleFlowClusterHO = cms.required.InputTag,
    Photons = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
