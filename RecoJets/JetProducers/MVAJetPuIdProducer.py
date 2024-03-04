import FWCore.ParameterSet.Config as cms

def MVAJetPuIdProducer(**kwargs):
  mod = cms.EDProducer('MVAJetPuIdProducer',
    runMvas = cms.bool(True),
    inputIsCorrected = cms.bool(True),
    vertexes = cms.InputTag('hltPixelVertices'),
    produceJetIds = cms.bool(True),
    jec = cms.string('AK4PF'),
    residualsFromTxt = cms.bool(False),
    applyJec = cms.bool(False),
    jetids = cms.InputTag(''),
    rho = cms.InputTag('hltFixedGridRhoFastjetAll'),
    jets = cms.InputTag('hltAK4PFJetsCorrected'),
    algos = cms.VPSet(
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
