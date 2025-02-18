import FWCore.ParameterSet.Config as cms

def CTPPSCompositeESSource(*args, **kwargs):
  mod = cms.ESSource('CTPPSCompositeESSource',
    compactViewTag = cms.string(''),
    lhcInfoLabel = cms.string(''),
    opticsLabel = cms.string(''),
    seed = cms.uint32(1),
    isRun2 = cms.bool(False),
    generateEveryNEvents = cms.untracked.uint32(1),
    verbosity = cms.untracked.uint32(0),
    periods = cms.VPSet(
      template = cms.PSetTemplate(
        L_int = cms.double(0),
        ctppsLHCInfo = cms.PSet(
          xangle = cms.double(-1),
          betaStar = cms.double(0),
          beamEnergy = cms.double(0),
          xangleBetaStarHistogramFile = cms.string(''),
          xangleBetaStarHistogramObject = cms.string('')
        ),
        ctppsOpticalFunctions = cms.PSet(
          opticalFunctions = cms.VPSet(
            template = cms.PSetTemplate(
              xangle = cms.required.double,
              fileName = cms.required.FileInPath
            )
          ),
          scoringPlanes = cms.VPSet(
            template = cms.PSetTemplate(
              rpId = cms.required.uint32,
              dirName = cms.required.string,
              z = cms.required.double
            )
          )
        ),
        ctppsRPAlignmentCorrectionsDataXML = cms.PSet(
          MeasuredFiles = cms.required.vstring,
          RealFiles = cms.required.vstring,
          MisalignedFiles = cms.required.vstring
        ),
        ctppsDirectSimuData = cms.PSet(
          empiricalAperture45 = cms.required.string,
          empiricalAperture56 = cms.required.string,
          timeResolutionDiamonds45 = cms.required.string,
          timeResolutionDiamonds56 = cms.required.string,
          efficienciesPerRP = cms.VPSet(
            template = cms.PSetTemplate(
              rpId = cms.required.uint32,
              file = cms.required.string,
              object = cms.required.string
            )
          ),
          efficienciesPerPlane = cms.VPSet(
            template = cms.PSetTemplate(
              rpId = cms.required.uint32,
              file = cms.required.string,
              object = cms.required.string
            )
          )
        )
      )
    ),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
