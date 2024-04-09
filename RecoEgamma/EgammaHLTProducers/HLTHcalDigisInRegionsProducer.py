import FWCore.ParameterSet.Config as cms

def HLTHcalDigisInRegionsProducer(**kwargs):
  mod = cms.EDProducer('HLTHcalDigisInRegionsProducer',
    outputProductNames = cms.vstring('EcalRegionalRecHitsEB'),
    inputCollTags = cms.VInputTag('hltHcalDigis'),
    etaPhiRegions = cms.VPSet(
      cms.PSet(
        inputColl = cms.InputTag('hltEgammaCandidates'),
        maxDEta = cms.double(0),
        maxDPhi = cms.double(0),
        maxDeltaR = cms.double(0.5),
        maxEt = cms.double(-1),
        minEt = cms.double(-1),
        type = cms.string('RecoEcalCandidate')
      )
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod