import FWCore.ParameterSet.Config as cms

def AlCaGammaJetSelector(*args, **kwargs):
  mod = cms.EDFilter('AlCaGammaJetSelector',
    PhoInput = cms.InputTag('gedPhotons'),
    PFjetInput = cms.InputTag('ak4PFJetsCHS'),
    MinPtJet = cms.double(10),
    MinPtPhoton = cms.double(10),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
