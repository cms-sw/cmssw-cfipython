import FWCore.ParameterSet.Config as cms

def BoostedDoubleSVProducer(**kwargs):
  mod = cms.EDProducer('BoostedDoubleSVProducer',
    beta = cms.double(1),
    R0 = cms.double(0.8),
    maxSVDeltaRToJet = cms.double(0.7),
    trackSelection = cms.PSet(),
    trackPairV0Filter = cms.PSet(
      k0sMassWindow = cms.double(0.03)
    ),
    svTagInfos = cms.InputTag('pfInclusiveSecondaryVertexFinderAK8TagInfos'),
    weights = cms.InputTag(''),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
