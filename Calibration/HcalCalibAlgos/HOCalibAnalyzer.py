import FWCore.ParameterSet.Config as cms

def HOCalibAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('HOCalibAnalyzer',
    hoCalibVariableCollectionTag = cms.InputTag('hoCalibProducer', 'HOCalibVariableCollection'),
    hoInputTag = cms.InputTag('horeco'),
    cosmic = cms.untracked.bool(True),
    zeroField = cms.untracked.bool(False),
    HOSignalBins = cms.untracked.int32(120),
    lowerRange = cms.untracked.double(-1),
    upperRange = cms.untracked.double(29),
    histFill = cms.untracked.bool(True),
    treeFill = cms.untracked.bool(False),
    sigma = cms.untracked.double(0.05),
    verbose = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
