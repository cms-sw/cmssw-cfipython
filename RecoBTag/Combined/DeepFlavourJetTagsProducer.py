import FWCore.ParameterSet.Config as cms

def DeepFlavourJetTagsProducer(*args, **kwargs):
  mod = cms.EDProducer('DeepFlavourJetTagsProducer',
    src = cms.InputTag('pfDeepCSVTagInfos'),
    checkSVForDefaults = cms.bool(False),
    meanPadding = cms.bool(False),
    NNConfig = cms.FileInPath('RecoBTag/Combined/data/DeepFlavourNoSL.json'),
    toAdd = cms.PSet(),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
