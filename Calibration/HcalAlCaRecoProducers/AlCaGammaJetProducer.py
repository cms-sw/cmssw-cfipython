import FWCore.ParameterSet.Config as cms

def AlCaGammaJetProducer(**kwargs):
  mod = cms.EDProducer('AlCaGammaJetProducer',
    PhoInput = cms.InputTag('gedPhotons'),
    PFjetInput = cms.InputTag('ak4PFJetsCHS'),
    HBHEInput = cms.InputTag('hbhereco'),
    HFInput = cms.InputTag('hfreco'),
    HOInput = cms.InputTag('horeco'),
    METInput = cms.InputTag('pfMet'),
    TriggerResults = cms.InputTag('TriggerResults', '', 'HLT'),
    gsfeleInput = cms.InputTag('gedGsfElectrons'),
    particleFlowInput = cms.InputTag('particleFlow'),
    VertexInput = cms.InputTag('offlinePrimaryVertices'),
    ConversionsInput = cms.InputTag('allConversions'),
    rhoInput = cms.InputTag('fixedGridRhoFastjetAll'),
    BeamSpotInput = cms.InputTag('offlineBeamSpot'),
    PhoLoose = cms.InputTag('PhotonIDProdGED', 'PhotonCutBasedIDLoose'),
    PhoTight = cms.InputTag('PhotonIDProdGED', 'PhotonCutBasedIDTight'),
    MinPtJet = cms.double(10),
    MinPtPhoton = cms.double(10),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
