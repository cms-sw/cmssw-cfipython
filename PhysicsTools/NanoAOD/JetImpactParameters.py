import FWCore.ParameterSet.Config as cms

def JetImpactParameters(*args, **kwargs):
  mod = cms.EDProducer('JetImpactParameters',
    jets = cms.InputTag('linkedObjectsCHS', 'jets'),
    pfCandidates = cms.InputTag('packedPFCandidates'),
    deltaRMax = cms.double(0.4),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
