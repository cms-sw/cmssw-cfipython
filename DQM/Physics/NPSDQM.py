import FWCore.ParameterSet.Config as cms

def NPSDQM(*args, **kwargs):
  mod = cms.EDProducer('NPSDQM',
    jetLabels = cms.vstring('ak4PFJetsCHS'),
    btagDeepCSV = cms.InputTag('pfDeepCSVJetTags', 'probb'),
    btagDeepJet = cms.InputTag('pfDeepFlavourJetTags', 'probb'),
    btagParticleNet = cms.InputTag('pfParticleNetAK4JetTags', 'probb'),
    btagRobustParT = cms.InputTag('pfParticleTransformerAK4JetTags', 'probb'),
    pfMETCollection = cms.InputTag('pfMet'),
    muonCollection = cms.InputTag('muons'),
    electronCollection = cms.InputTag('gedGsfElectrons'),
    photonCollection = cms.InputTag('gedPhotons'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
