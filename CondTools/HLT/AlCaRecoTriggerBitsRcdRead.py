import FWCore.ParameterSet.Config as cms

def AlCaRecoTriggerBitsRcdRead(**kwargs):
  mod = cms.EDAnalyzer('AlCaRecoTriggerBitsRcdRead',
    rawFileName = cms.untracked.string(''),
    outputType = cms.untracked.string('twiki'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
