import FWCore.ParameterSet.Config as cms

def PixelCPETemplateRecoESProducer(**kwargs):
  mod = cms.ESProducer('PixelCPETemplateRecoESProducer',
    LoadTemplatesFromDB = cms.bool(True),
    Alpha2Order = cms.bool(True),
    ClusterProbComputationFlag = cms.int32(0),
    useLAWidthFromDB = cms.bool(True),
    lAOffset = cms.double(0),
    lAWidthBPix = cms.double(0),
    lAWidthFPix = cms.double(0),
    doLorentzFromAlignment = cms.bool(False),
    useLAFromDB = cms.bool(True),
    barrelTemplateID = cms.int32(0),
    forwardTemplateID = cms.int32(0),
    directoryWithTemplates = cms.int32(0),
    speed = cms.int32(-2),
    UseClusterSplitter = cms.bool(False),
    ComponentName = cms.string('PixelCPETemplateReco'),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
