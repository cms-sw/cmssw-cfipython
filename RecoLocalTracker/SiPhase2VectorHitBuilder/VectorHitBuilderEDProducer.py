import FWCore.ParameterSet.Config as cms

def VectorHitBuilderEDProducer(**kwargs):
  mod = cms.EDProducer('VectorHitBuilderEDProducer',
    offlinestubs = cms.string('vectorHits'),
    maxVectorHits = cms.int32(999999999),
    Algorithm = cms.ESInputTag('', 'SiPhase2VectorHitMatcher'),
    CPE = cms.ESInputTag('phase2StripCPEESProducer', 'Phase2StripCPE'),
    BarrelCut = cms.vdouble(
      0,
      0.05,
      0.06,
      0.08,
      0.09,
      0.12,
      0.2
    ),
    Clusters = cms.string('siPhase2Clusters'),
    maxVectorHitsInAStack = cms.int32(999),
    EndcapCut = cms.vdouble(
      0,
      0.1,
      0.1,
      0.1,
      0.1,
      0.1
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
