import FWCore.ParameterSet.Config as cms

def EgammaHLTPixelMatchVarProducer(*args, **kwargs):
  mod = cms.EDProducer('EgammaHLTPixelMatchVarProducer',
    recoEcalCandidateProducer = cms.InputTag('hltL1SeededRecoEcalCandidate'),
    pixelSeedsProducer = cms.InputTag('electronPixelSeeds'),
    dPhi1SParams = cms.PSet(
      bins = cms.required.VPSet
    ),
    dPhi2SParams = cms.PSet(
      bins = cms.required.VPSet
    ),
    dRZ2SParams = cms.PSet(
      bins = cms.required.VPSet
    ),
    productsToWrite = cms.int32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
