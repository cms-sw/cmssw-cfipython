import FWCore.ParameterSet.Config as cms

def AlCaRecoTriggerBitsRcdRead(*args, **kwargs):
  mod = cms.EDAnalyzer('AlCaRecoTriggerBitsRcdRead',
    rawFileName = cms.untracked.string(''),
    outputType = cms.untracked.string('twiki'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
