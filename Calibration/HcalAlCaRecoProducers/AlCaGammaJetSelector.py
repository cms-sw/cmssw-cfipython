import FWCore.ParameterSet.Config as cms

def AlCaGammaJetSelector(**kwargs):
  mod = cms.EDFilter('AlCaGammaJetSelector',
    PhoInput = cms.InputTag('gedPhotons'),
    PFjetInput = cms.InputTag('ak4PFJetsCHS'),
    MinPtJet = cms.double(10),
    MinPtPhoton = cms.double(10),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
