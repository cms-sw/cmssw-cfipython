import FWCore.ParameterSet.Config as cms

def SiStripBadStripFromQualityDBWriter(**kwargs):
  mod = cms.EDProducer('SiStripBadStripFromQualityDBWriter',
    record = cms.string(''),
    OpenIovAt = cms.untracked.string('beginOfTime'),
    OpenIovAtTime = cms.untracked.uint32(1),
    StripQualityLabel = cms.string(''),
    BadComponentsFromFedErrors = cms.PSet(
      Add = cms.bool(False),
      Cutoff = cms.double(0.8),
      LegacyDQMFile = cms.string(''),
      FileRunNumber = cms.uint32(4294967295)
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
